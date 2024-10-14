package main

import (
	"net/http"

	"github.com/julienschmidt/httprouter"
)

func (app *application) routes() *httprouter.Router {

	router := httprouter.New()

	//Health Check Routes
	router.HandlerFunc(http.MethodGet, "/", app.healthcheckHandler)

	//Picks And Standings Routes
	router.HandlerFunc(http.MethodGet, "/v1/login", app.allSeasonStandings)
	router.HandlerFunc(http.MethodGet, "/v1/register", app.seasonStandings)

	//Picks And Standings Routes
	router.HandlerFunc(http.MethodPost, "/v1/lockin_picks", app.allSeasonStandings)
	router.HandlerFunc(http.MethodGet, "/v1/get_picks", app.allSeasonStandings)

	router.HandlerFunc(http.MethodGet, "/v1/picks_standings", app.allSeasonStandings)
	router.HandlerFunc(http.MethodGet, "/v1/picks_standings/season", app.allSeasonStandings)

	router.HandlerFunc(http.MethodGet, "/v1/nfl_standings", app.allSeasonStandings)
	router.HandlerFunc(http.MethodGet, "/v1/nfl_standings/season", app.allSeasonStandings)

	return router
}
