// const numbers = [1, 2, 3, 4, 5];
// const [x, y] = numbers;
// const [a, b, c, d, e, f] = numbers;

// const user = { username: 'beomjun', age:17};
// const {username, address} = user;

// console.log(username)
// console.log(address)
// console.log(user)
// console.log(x)
// console.log(y)
// console.log()
// console.log(a)
// console.log(b)
// console.log(c)
// console.log(d)
// console.log(e)
// console.log(f)

const getTime = () => {
    return new Promise((resolve, reject) => {
        setTimeout(function () {
            resolve(Date.now());
        }, 1000);
    });
};

const getServerTime = async () => {
    try {
        const ts = await getTime();
        console.log(ts);
        console.log('getServerTime');
    } catch (e) {
        console.error(e);
    }
};
getServerTime();