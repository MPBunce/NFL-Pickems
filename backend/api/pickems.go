package main

import (
	"context"
	"encoding/json"
	"net/http"

	"github.com/julienschmidt/httprouter"
	"go.mongodb.org/mongo-driver/bson"
)

func (app *application) allSeasonStandings(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {

	var data []SeasonStandings
	collection := app.dbClient.Database("NFL-Pickems").Collection("Season Standings")
	cursor, err := collection.Find(context.TODO(), bson.D{})
	if err != nil {
		panic(err)
	}
	if err = cursor.All(context.TODO(), &data); err != nil {
		panic(err)
	}

	// fmt.Println("displaying all results from the search query")
	// for _, result := range data {
	// 	fmt.Println(result)
	// 	fmt.Println("\n")
	// }
	if data == nil {
		http.Error(w, "Data Not Found", http.StatusNotFound)
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
		panic(err)
	}
	if err = cursor.All(context.TODO(), &data); err != nil {
		panic(err)
	}

	// fmt.Println("displaying all results from the search query")
	// for _, result := range data {
	// 	fmt.Println(result)
	// 	fmt.Println("\n")
	// }
	if data == nil {
		http.Error(w, "Data Not Found", http.StatusNotFound)
		return
	}

	json.NewEncoder(w).Encode(data)
}
