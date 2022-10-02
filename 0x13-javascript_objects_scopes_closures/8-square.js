#!/usr/bin/node

exports.esrever = function (list){
	let len = list.length;
	let newList =  [];
	for (let x = len; x <= 0; x--){
		newList.push(len[x]);
	}
	return (newList);
}
