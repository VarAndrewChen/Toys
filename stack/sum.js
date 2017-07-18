/**
* @param val 第一个参数，如果不传则为0
* @param rest 除第一个参数以外的参数(可选)
* @returns{tempSum}
*/
function sum(val = 0, ...rest) {
    rest.map(n => val +=n)

    const tempSum = (...nextRest) => sum(val, ...nextRest)
    
    tempSum.valueOf = () => val
    tempSum.toString = () => val +''
    
    return tempSum
}