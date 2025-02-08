package main

import (
	"go.mongodb.org/mongo-driver/bson/primitive"
)

type SeasonStandings struct {
	ID    primitive.ObjectID `json:"id" bson:"_id,omitempty"`
	Year  string             `json:"year" bson:"year"`
	Teams []TeamData         `json:"teams" bson:"teams"`
}

type TeamData struct {
	Team         string `json:"team" bson:"team"`
	Wins         int    `json:"wins" bson:"wins"`
	Losses       int    `json:"losses" bson:"losses"`
	Ties         int    `json:"ties" bson:"ties"`
	Division     string `json:"division" bson:"division"`
	DivisionRank int    `json:"division_rank" bson:"division_rank"`
	Year         string `json:"year" bson:"year"`
}

type UserProfile struct {
	Id         string `json:"id" bson:"_id,omitempty"`
	Email      string `bson:"email"`
	Name       string `bson:"name"`
	ProfilePic string `bson:"profilePic"`
}

type UserPicks struct {
	Id    string      `json:"id" bson:"_id,omitempty"`
	Year  string      `json:"year" bson:"year"`
	Picks []UserGuess `json:"picks" bson:"picks"`
}

type UserGuess struct {
	Team         string `json:"team" bson:"team"`
	Division     string `json:"division" bson:"division"`
	DivisionRank int    `json:"division_rank" bson:"division_rank"`
	Year         string `json:"year" bson:"year"`
}

type LeaderBoard struct {
	Id    string 
	Name  string 
	Picture  string 
	Score int    
}
