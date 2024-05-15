#!/usr/bin/node

let fs = require('fs')

fs.readFile('my_file.txt', 'utf-8', function(err, data){
    try{
        if(data){
            console.log(data)
            }
        }
        catch(err){
            print(err)
        }
    

})