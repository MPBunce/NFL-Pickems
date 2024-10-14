package main

import (
	"context"
	"fmt"
	"net/http"
	"strconv"

	"github.com/julienschmidt/httprouter"
	"go.mongodb.org/mongo-driver/bson"
)

func (app *application) allSeasonStandings(w http.ResponseWriter, r *http.Request) {

	filter := bson.D{}
	collection := app.dbClient.Database("NFL-Pickems").Collection("Season Standings")
	res, err := collection.Find(context.TODO(), filter)
	if err != nil {
		app.logger.Printf("Error: %s", err)
	}

	fmt.Fprintln(w, "%s", res)

}

func (app *application) seasonStandings(w http.ResponseWriter, r *http.Request) {
	//sort := bson.D{{"date_ordered", 1}}
	params := httprouter.ParamsFromContext(r.Context())

	id, err := strconv.ParseInt(params.ByName("id"), 10, 64)
	if err != nil || id < 1 {
		http.NotFound(w, r)
		return
	}

	fmt.Fprintf(w, "show the details of movie %d\n", id)
}
