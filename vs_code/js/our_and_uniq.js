
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

function ours(array,array2){
    let array3=[]
    for (let i=0;i<array2.length;i++){
        if (array2[i] in array) array3.push(array2[i])
    }
    return array3
}
console.log(ours(array,array2))
