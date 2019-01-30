require(`dotenv`).config();

var ToneAnalyzerV3 = require('watson-developer-cloud/tone-analyzer/v3');

let text = "Hi my name is madi and I love cake and everything cheerful!";

let toneAnalyzer = new ToneAnalyzerV3({
    username: process.env.IBM_USER,
    password: process.env.IBM_PASSWORD,
    version: '2017-09-21',
    url: 'https://gateway.watsonplatform.net/tone-analyzer/api/'
});

toneAnalyzer.tone(
    {
        tone_input: text,
        content_type: 'text/plain'
    },
    function(err, tone) {
        if (err) {
            console.log(err);
        } else {
            console.log(JSON.stringify(tone, null, 2));
        }
    }
);
