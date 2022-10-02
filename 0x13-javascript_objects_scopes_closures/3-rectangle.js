#!/usr/bin/node

class Rectangle {
	constructor(w, h){
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h
		}
	}
	print() {
		for (let x = 0; x <= this.height; x++){
			for (let y = 0; y <= this.width; y++){
				console.log("X");
			}
			console.log("\n");
		}
	}
}
