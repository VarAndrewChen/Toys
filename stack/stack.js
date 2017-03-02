/*jshint esversion: 6 */
class Stack {
    constructor(props) {
        this.items = [];
    }
    push(ele) {
        this.items.push(ele);
    }
    pop() {
        return this.items.pop();
    }
    peek() {
        return this.items[this.items.length - 1];
    }
    isEmpty() {
        return this.items.length === 0;
    }
    size() {
        return this.items.length;
    }
    clear() {
        return this.items = [];
    }
    print() {
        console.log(this.items.toString());
    }
}

function divideBy2(decNumber) {
    let remStack = new Stack(),
        rem,
        binaryString = '';
    while (decNumber > 0) {
        rem = Math.floor(decNumber % 2);
        remStack.push(rem);
        decNumber = Math.floor(decNumber / 2);
    }
    while (!remStack.isEmpty()) {
        binaryString += remStack.pop().toString();
    }
    return binaryString;
}

function baseConverter(decNumber, base) {
    let remStack = new Stack(),
        rem,
        baseString = '',
        digits = '0123456789ABCDEF';
    while (decNumber > 0) {
        rem = Math.floor(decNumber % base);
        remStack.push(rem);
        decNumber = Math.floor(decNumber / base);
    }
    while (!remStack.isEmpty()) {
        baseString += digits[remStack.pop()];
    }
    return baseString;
}
