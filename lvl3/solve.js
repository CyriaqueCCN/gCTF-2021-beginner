groups = {}
/*
const result = a.reduce((r, n) => {
  const lastSubArray = r[r.length - 1];

  if(!lastSubArray || lastSubArray[lastSubArray.length - 1] !== n - 1) {
    r.push([]);
  }

  r[r.length - 1].push(n);

  return r;
}, []);
*/
var last_dist = 999;
var penult_dist = 998;
var groups = {};
var sc = scanArray;
for (var i = 0 ; i < sc.length ; i++) {
	if (sc[i] > 0 && sc[i] == last_dist && sc[i] == penult_dist) {
		groups[i - 1] = sc[i];
	} else if (sc[i] == last_dist && sc[i] > 0) {
 		groups[i] = sc[i]
	}
	penult_dist = last_dist;
	last_dist = sc[i];
}

target = -1;
furthest = -1;
for (var k in groups) {
	if (groups[k] > furthest) {
		furthest = groups[k];
		target = k;
	}
}

console.log(sc);
console.log(groups);
console.log(target, furthest);

return target - 8;

// scanArray = [0, 0, 0, 74, 74, 74, 999, 21, 21, 21, 999, 20, 20, 20, 0, 0, 0];

// game is bugged : sometimes the scan array looks like
/* [
  0,
  0,
  0,
  0,
  0,
  3.25,
  3.25,
  3.25,
  3,
  3,
  3,
  3,
  17,
  17,
  0,
  0,
  0
]*/
