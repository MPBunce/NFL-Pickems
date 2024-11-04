package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/julienschmidt/httprouter"
	"go.mongodb.org/mongo-driver/bson"
	"google.golang.org/api/idtoken"
)

func (app *application) lockinPicks(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {

	tokenString := r.Header.Get("Authorization")
	payload, err := idtoken.ParsePayload(tokenString)
	if err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Error with google auth token"})
		return
	}
	if checkUser := app.confirmUser(payload.Subject); checkUser != true {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Error finding user"})
		return
	}

	year := ps.ByName("year")
	//Parse User Picks
	decoder := json.NewDecoder(r.Body)
	var inputPicks []UserGuess
	e := decoder.Decode(&inputPicks)
	if e != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error"})
		return
	}
	if inputPicks == nil || len(inputPicks) != 32 {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bad picks"})
		return
	}

	userPicks := UserPicks{
		Id:    payload.Subject,
		Year:  year,
		Picks: inputPicks,
	}

	//confirm there are no pics for that year
	var data []UserPicks
	filter := bson.D{{"_id", payload.Subject}, {"year", year}}

	collection := app.dbClient.Database("NFL-Pickems").Collection("UserPicks")
	cursor, err := collection.Find(context.TODO(), filter)

	if err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error"})
		return
	}
	if err = cursor.All(context.TODO(), &data); err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error"})
		return
	}
	if data != nil {
		w.WriteHeader(http.StatusBadRequest)
		json.NewEncoder(w).Encode(map[string]string{"error": "You already locked in your picks for this year!"})
		return
	}

	res, e := collection.InsertOne(context.TODO(), userPicks)
	if e != nil {
		fmt.Println("Error Inserting Record")
	}
	fmt.Println("Creating Picks")
	json.NewEncoder(w).Encode(res)
	return

}

func (app *application) getPicks(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {

	year := ps.ByName("year")
	tokenString := r.Header.Get("Authorization")
	payload, err := idtoken.ParsePayload(tokenString)
	if err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Error with google auth token"})
		return
	}
	if checkUser := app.confirmUser(payload.Subject); checkUser != true {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Error finding user"})
		return
	}

	var data []UserPicks
	filter := bson.D{{"_id", payload.Subject}, {"year", year}}

	collection := app.dbClient.Database("NFL-Pickems").Collection("UserPicks")
	cursor, err := collection.Find(context.TODO(), filter)
	if err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error"})
		return
	}
	if err = cursor.All(context.TODO(), &data); err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error"})
		return
	}

	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(data)

}

func (app *application) picksStandings(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {

}

func (app *application) confirmUser(subject string) bool {

	var data []UserProfile
	filter := bson.D{{"_id", subject}}
	collection := app.dbClient.Database("NFL-Pickems").Collection("UserProfile")

	cursor, err := collection.Find(context.TODO(), filter)
	if err != nil {
		return false
	}
	if err = cursor.All(context.TODO(), &data); err != nil {
		return false
	}

	if len(data) == 1 {
		return true
	} else {
		return false
	}

}
