#!/usr/bin/node

import Square from './5-square.js'

class Square extends Square {
	charPrint(c){
		if (c) {
			print(c);
		} else {
			print("X");
		}
}
