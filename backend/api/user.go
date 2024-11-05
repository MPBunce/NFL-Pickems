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

func (app *application) getUser(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
	//CORS
	enableCors(&w)

	tokenString := r.Header.Get("Authorization")
	payload, err := idtoken.ParsePayload(tokenString)
	if err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Error with google auth token"})
		return
	}

	doc := UserProfile{
		Id:         payload.Subject,
		Email:      payload.Claims["email"].(string),
		Name:       payload.Claims["name"].(string),
		ProfilePic: payload.Claims["picture"].(string),
	}

	var data []UserProfile
	filter := bson.D{{"_id", payload.Subject}}
	collection := app.dbClient.Database("NFL-Pickems").Collection("UserProfile")

	cursor, err := collection.Find(context.TODO(), filter)
	if err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Issue connecting to DB"})
		return
	}
	if err = cursor.All(context.TODO(), &data); err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Issue with DB cursor"})
		return
	}

	fmt.Println(len(data))

	if len(data) == 0 {
		res, e := collection.InsertOne(context.TODO(), doc)
		if e != nil {
			fmt.Println("Error Inserting Record")
		}
		fmt.Println("Created Record")
		json.NewEncoder(w).Encode(res)
		return
	} else if len(data) == 1 {
		//if len 1 one record
		fmt.Println("User Exists")
		json.NewEncoder(w).Encode(data[0])
		return
	} else {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Resource not found"})
		return
	}

}
