## Brief

 Vienna - Chemical plant
"You must wonder why we have summoned you, AGENT? It has come to our attention that something terrible is about to take place. There is still time to prevent the disaster, and we could not think of anyone more suited for this task than you. We believe that if you can’t solve this quest, neither can anybody else. You have to travel to Vienna, and investigate a suspicious chemical plant. This mission must be executed in secrecy. It’s classified, and it regards the safety of the whole world, therefore we can’t tell you anything more just yet. Go now, you have the fate of the world in your hands."

Challenge: CCTV (rev)
You arrive at your destination. The weather isn't great, so you figure there's no reason to stay outside and you make your way to one of the buildings. No one bothered you so far, so you decide to play it bold - you make yourself a cup of coffee in the social area like you totally belong here and proceed to find an empty room with a desk and a chair. You pull out our laptop, hook it up to the ethernet socket in the wall, and quickly find an internal CCTV panel - that's a way better way to look around unnoticed. Only problem is... it wants a password.

## Link

https://cctv-web.2021.ctfcompetition.com/

## Solve

Right clic -> Display source -> see JS file

```js
const checkPassword = () => {
  const v = document.getElementById("password").value;
  const p = Array.from(v).map(a => 0xCafe + a.charCodeAt(0));

  if(p[0] === 52037 &&
     p[6] === 52081 &&
     p[5] === 52063 &&
     p[1] === 52077 &&
     p[9] === 52077 &&
     p[10] === 52080 &&
     p[4] === 52046 &&
     p[3] === 52066 &&
     p[8] === 52085 &&
     p[7] === 52081 &&
     p[2] === 52077 &&
     p[11] === 52066) {
    window.location.replace(v + ".html");
  } else {
    alert("Wrong password!");
  }
}
```

Well, quite easy :

```js
function reverse() {
	var p = new Array(12);
	p[0] = String.fromCharCode(52037 - 0xcafe);
     p[6] = String.fromCharCode(52081  - 0xcafe);
     p[5] = String.fromCharCode(52063  - 0xcafe);
     p[1] = String.fromCharCode(52077  - 0xcafe);
     p[9] = String.fromCharCode(52077 - 0xcafe);
     p[10] = String.fromCharCode(52080 - 0xcafe);
     p[4] = String.fromCharCode(52046 - 0xcafe);
     p[3] = String.fromCharCode(52066 - 0xcafe);
     p[8] = String.fromCharCode(52085 - 0xcafe);
     p[7] = String.fromCharCode(52081 - 0xcafe);
     p[2] = String.fromCharCode(52077 - 0xcafe);
     p[11] = String.fromCharCode(52066 - 0xcafe);
	console.log(p);
};
reverse()
```
Outputs :
```
0: "G"
​
1: "o"
​
2: "o"
​
3: "d"
​
4: "P"
​
5: "a"
​
6: "s"
​
7: "s"
​
8: "w"
​
9: "o"
​
10: "r"
​
11: "d"
​
length: 12
```

We enter "GoodPassword"

Flag is `CTF{IJustHopeThisIsNotOnShodan}`

