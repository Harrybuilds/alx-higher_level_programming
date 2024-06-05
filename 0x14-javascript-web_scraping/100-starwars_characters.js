#!/usr/bin/node

const request = require('request')

const getNames = (movieId) => {
    const options = {
	uri: `https://swapi-api.alx-tools.com/api/films/${movieId}`,
	method: "GET",
	json: true
    }

    request(options, (err, res, body)=>{
	if (err){
	    console.error(err);
	}
	const xter = body.characters
	for (let i=0; i < xter.length; i++){
	    const req = {
		uri: xter[i],
		method: 'GET',
		json: true
	    }
	    request(req, (err, res, body) => {
		if (err){
		    console.error(err);
		}
		console.log(body.name)
	    });
	}
    })
}

const id = process.argv[2]

getNames(id);
