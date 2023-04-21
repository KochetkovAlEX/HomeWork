function f(a,b){
    if(a<b) return -1
    if (a==b) return 0
    if (a>b) return 1
}

let a=+prompt()
let b=+prompt()
console.log(f(a,b))

function fact(n){
    if(n==1) return 1;
    return n*fact(n-1);
}

let n=+prompt()
console.log(fact(n))



function combine(n1,n2,n3){
    return Number(n1+n2+n3)
}
let n1=prompt("Число 1")
let n2=prompt("Число 2")
let n3=prompt("Число 2")
console.log(combine(n1,n2,n3))

function s(a,b){
    if (b!=" " && a!=" ")return a*b
    return a*a
}
a=+prompt()
b=+prompt()
console.log(s(a,b))

function amazing_num(num){
     count=0
    for (let i=0;i<num;i+=1){
        if (num%i==0) count+=i
        else continue
    }
    if (num==count) return "yes"
    else{
        return "no"
    }

}

num=+prompt("Введите возможное совершенное число:")
console.log(amazing_num(num))


function amazing_num(num1,num2){
    while(num1<=num2){
        let count=0
        for(let i=0;i<num1;i+=1){
        if (num1%i==0) count+=i 
        }
    if(count==num1) console.log(num1)
    num1+=1
    }
}
min=+prompt("Введите минимальное число:")
max=+prompt("Введите максимальное число: ")
amazing_num(min,max)

function time(h,min,sec){
    if (h<10) h="0"+String(h)
    if (min<10) min="0" + String(min)
    if (min==" ") min="00"
    if (sec<10) sec="0" + String(sec) 
    if (sec==" ") sec="00"
    return `${h}:${min}:${sec}`
}
h=+prompt("Введите часы")
min=+prompt("Введите минуты")
sec=+prompt("Введите секунды")
console.log(time(h,min,sec))


function seconds(h,min,sec){
    return time=h*3600 + min*60 + sec
}
h=+prompt("Введите часы")
min=+prompt("Введите минуты")
sec=+prompt("Введите секунды")
console.log(seconds(h,min,sec))

function hour(sec){
    h=Math.round(sec/3600)
    min=Math.round((sec-3600*h)/60)
    seconds=sec-h*3600-min*60
    if (h<10) h="0"+String(h)
    if (min<10) min="0" + String(min)
    if (sec<10) sec="0" + String(sec) 
    return `${h}:${min}:${seconds}`
}

console.log(hour(7700))



function dif(h1,min1,sec1,h2,min2,sec2){
    time1=h1*3600 + min1*60 + sec1
    time2=h2*3600 + min2*60 + sec2
    if (time1>time2) time3=time1-time2
    else return "Отрицательное время? Физика для тебя шутка?"
    h3=Math.floor(time3/3600)
    min3=Math.round((time3-3600*h3)/60)
    sec3=time3-h3*3600-min3*60
    if (h3<10) h3="0"+String(h3)
    if (min3<10) min3="0" + String(min3)
    if (sec3<10) sec3="0" + String(sec3) 
    return `${h3}:${min3}:${sec3}`
}
h1=+prompt("Введите часы 1:")
min1=+prompt("Введите минуты 1:")
sec1=+prompt("Введите секунды 1:")
h2=+prompt("Введите часы 2:")
min2=+prompt("Введите минуты 2:")
sec2=+prompt("Введите секунды 2:")
console.log(dif(h1,min1,sec1,h2,min2,sec2))
