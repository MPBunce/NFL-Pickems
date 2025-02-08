package main

import (
	"context"
	"encoding/json"
	"net/http"

	"github.com/julienschmidt/httprouter"
	"go.mongodb.org/mongo-driver/bson"
)

func (app *application) allSeasonStandings(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {

	var data []SeasonStandings
	collection := app.dbClient.Database("NFL-Pickems").Collection("Season Standings")

	cursor, err := collection.Find(context.TODO(), bson.D{})
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

	if data == nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error"})
		return
	}
	json.NewEncoder(w).Encode(data)

}

func (app *application) seasonStandings(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {

	year := ps.ByName("year")
	var data []SeasonStandings
	filter := bson.D{{"year", year}}

	collection := app.dbClient.Database("NFL-Pickems").Collection("Season Standings")
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

	if data == nil {
		http.Error(w, "Data Not Found", http.StatusNotFound)
		return
	}
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(data[0])
}
