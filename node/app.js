require('log-timestamp')(function() { return `${new Date().toISOString()} %s` });

var AWS = require('aws-sdk');

var sts = new AWS.STS();


let main = async (name) => {
    // Object.keys(process.env).forEach(key => {
    //     console.log(`${key}=${process.env[key]}`);
    // });
    console.log(`Hello, ${name}`);
    sts.getCallerIdentity({}, function (err, data) {
        if (err) console.log(err, err.stack);
        else console.log(data);
    })
}

main("World");