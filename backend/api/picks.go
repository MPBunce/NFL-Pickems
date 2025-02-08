package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
	"sort"
	"github.com/julienschmidt/httprouter"
	"go.mongodb.org/mongo-driver/bson"
	"google.golang.org/api/idtoken"
)

func (app *application) lockinPicks(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {

	tokenString := r.Header.Get("Authorization")
	payload, err := idtoken.ParsePayload(tokenString)
	if err != nil {
		w.WriteHeader(http.StatusUnauthorized)
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
		json.NewEncoder(w).Encode(map[string]string{"error": "User has picks"})
		return
	}
	if inputPicks == nil || len(inputPicks) != 32 {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Array Len?"})
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
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error 2"})
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
		w.WriteHeader(http.StatusUnauthorized)
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
	if data == nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "data not found"})
		return
	}
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(data[0])

}

func (app *application) picksStandings(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {

	var userPicks []UserPicks;
	var userProfile []UserProfile;
	var seasonStandings []SeasonStandings;
	year := ps.ByName("year");
	filter := bson.D{}


	collection := app.dbClient.Database("NFL-Pickems").Collection("UserProfile")
	cursor, err := collection.Find(context.TODO(), filter)
	if err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error"})
		return
	}
	if err = cursor.All(context.TODO(), &userProfile); err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error"})
		return
	}

	filterByYear := bson.D{{"year", year}}

	collectionTwo := app.dbClient.Database("NFL-Pickems").Collection("UserPicks")
	cursorTwo, errTwo := collectionTwo.Find(context.TODO(), filterByYear)
	if errTwo != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error"})
		return
	}
	if errTwo = cursorTwo.All(context.TODO(), &userPicks); err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error"})
		return
	}

	collectionThree := app.dbClient.Database("NFL-Pickems").Collection("Season Standings")
	cursorThree, errThree := collectionThree.Find(context.TODO(), filterByYear)
	if errThree != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error"})
		return
	}
	if errThree = cursorThree.All(context.TODO(), &seasonStandings); err != nil {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{"error": "Bruh Error"})
		return
	}

	output := app.calcLeaderBoard(userPicks, userProfile, seasonStandings[0]);
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(output)


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

func (app *application) calcLeaderBoard(userPicks []UserPicks, userProfiles []UserProfile,  seasonStandings SeasonStandings) []LeaderBoard {

	var output []LeaderBoard

	for _, user := range userProfiles {
		score := 0

		// Find the user's picks
		for _, picks := range userPicks {
			if picks.Id == user.Id { // Match user ID to their picks
				fmt.Println("Processing picks for:", user.Name)
				// Compare each pick with the actual standings
				for _, pick := range picks.Picks {
					fmt.Println("User Pick:", pick) 
					for _, team := range seasonStandings.Teams {
						// Normalize and compare team name, division, and ranking
						if(strings.ToLower(strings.TrimSpace(team.Team)) == strings.ToLower(strings.TrimSpace(pick.Team))) && pick.DivisionRank == team.DivisionRank {
							fmt.Println("works!")
							fmt.Println("Pick Rank: ", pick.DivisionRank, "Standing Rank", team.DivisionRank)
							fmt.Println(pick.DivisionRank == team.DivisionRank)
							score += 1
						}

					}
				}
			}
		}

		// Create leaderboard entry
		entry := LeaderBoard{
			Id:      user.Id,
			Name:    user.Name,
			Picture: user.ProfilePic,
			Score:   score,
		}

		// Append to output slice
		output = append(output, entry)
	}
	sort.Slice(output, func(i, j int) bool {
		return output[i].Score > output[j].Score // Highest scores first
	})
	return output

}
