// function f(a,b){
//     if(a<b) return -1
//     if (a==b) return 0
//     if (a>b) return 1
// }

// let a=+prompt()
// let b=+prompt()
// console.log(f(a,b))

// function fact(n){
//     if(n==1) return 1;
//     return n*fact(n-1);
// }

// let n=+prompt()
// console.log(fact(n))



// function combine(n1,n2,n3){
//     return Number(n1+n2+n3)
// }
// let n1=prompt("Число 1")
// let n2=prompt("Число 2")
// let n3=prompt("Число 2")
// console.log(combine(n1,n2,n3))

// function s(a,b){
//     if (b!=" " && a!=" ")return a*b
//     return a*a
// }
// a=+prompt()
// b=+prompt()
// console.log(s(a,b))

// function amazing_num(num){
//      count=0
//     for (let i=0;i<num;i+=1){
//         if (num%i==0) count+=i
//         else continue
//     }
//     if (num==count) return "yes"
//     else{
//         return "no"
//     }

// }

// num=+prompt("Введите возможное совершенное число:")
// console.log(amazing_num(num))

//!не понял
// function amazing_num(num){
//     let count=0
//     for (let i=1;i<num;i+=1){
//         for (let b=1;b<i;b+=1){
//             if(i%b==0) count+=b
//         }
//         if (i==count) return i
//     }
//   }
//   num=+prompt("Введите возможное совершенное число:")
//   console.log(amazing_num(num))

// function time(h,min,sec){
//     if (h<10) h="0"+String(h)
//     if (min<10) min="0" + String(min)
//     if (min==" ") min="00"
//     if (sec<10) sec="0" + String(sec) 
//     if (sec==" ") sec="00"
//     return `${h}:${min}:${sec}`
// }
// h=+prompt("Введите часы")
// min=+prompt("Введите минуты")
// sec=+prompt("Введите секунды")
// console.log(time(h,min,sec))


// function seconds(h,min,sec){
//     return time=h*3600 + min*60 + sec
// }
// h=+prompt("Введите часы")
// min=+prompt("Введите минуты")
// sec=+prompt("Введите секунды")
// console.log(seconds(h,min,sec))


const array=[1,2,3,4], array2=[1,2,7]
    function uniq(array,array2){
    let array3=[]
    for (let i=0;i<array2.length;i++){
        if (!(array2[i] in array)) array3.push(array2[i])
    }
    for (let i=0;i<array.length;i++){
        if (!(array[i] in array2)) array3.push(array[i])
    }
    array3.sort()
    return array3
}
console.log(uniq(array,array2))