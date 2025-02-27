package main

import (
	"net/http"

	"github.com/julienschmidt/httprouter"
)

func (app *application) routes() *httprouter.Router {

	router := httprouter.New()

	//Health Check Routes
	router.HandlerFunc(http.MethodGet, "/", app.healthcheckHandler)

	//Season Routes
	router.GET("/v1/seasons", app.allSeasonStandings)
	router.GET("/v1/seasons/:year", app.seasonStandings)

	//User Profile
	router.GET("/v1/user", app.getUser)

	//Picks
	router.GET("/v1/get/picks/:year", app.getPicks)
	router.POST("/v1/lockin/picks/:year", app.lockinPicks)

	//Leaderboard
	router.GET("/v1/leaderboard/:year", app.picksStandings)

	return router
}
