var obj = {
	x:'hello',
	y:'word',
	z:function(){
		console.log('nihao')
	},
	a:{
		t:'ohayo',
		h:function(){
			console.log('test')
		}
	},
};
obj.z();
obj.a.h();
console.log(obj.a.t);