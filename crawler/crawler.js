const puppeteer = require("puppeteer");
const fs = require('fs');
var HTMLParser = require('node-html-parser');
var stdin = process.openStdin();
stdin.setRawMode( true );
stdin.resume();
stdin.setEncoding( 'utf8' );

const selectors_1 = ("" + fs.readFileSync("common_1.css")).split("\n").join(" ");
const selectors_2 = ("" + fs.readFileSync("common_2.css")).split("\n").join(" ");

const checkPage = async (url) => {
    const browser = await puppeteer.launch({
        devtools: false,
        headless: true,
        // ignoreDefaultArgs: ["--disable-extensions","--enable-automation"],
        // args: [
        //     // `--start-maximized`,
        //     `--load-extension=/home/maxence/.config/google-chrome/Default/Extensions/fihnjjcciajhdojfnbdddfaoknhalnja/3.4.3_0`
        // ]
    });
    const page = (await browser.pages())[0];
    stdin.on('data', async function(key) { 
        if ( key === '\u0003' ) {
            process.exit();
        }
        if (key === '*') {
            fs.appendFile("results.txt", url+"\n", err => {
                if (err) {
                    console.error(err);
                }
            });
        }
    });
    //const cdpClient = await page.target().createCDPSession();
    // await cdpClient.send('Log.enable');

    // cdpClient.on('Log.entryAdded', async ({ entry }) => {
    //   console.log(entry);
    // });

    try {
        await page.goto(url, {waitUntil: 'domcontentloaded',timeout: 10000});

        await new Promise(r => setTimeout(r, 4000));
        var html = await page.content();
        var document = HTMLParser.parse(html);
        if ((document.querySelector(selectors_1) != null) || (document.querySelector(selectors_2) != null)) {
            console.log(url);
            fs.appendFile("results.txt", url+"\n", err => {
                if (err) {
                    console.error(err);
                }
            });
        }
        await browser.close();
    }
    catch {
       await browser.close();
    }
    //setTimeout(() => {browser.close()}, 4000);
}

const runCrawler = async (urls) => {
    for (u of urls) {
        u = u.split(",")[1];
        console.log(u);
        if (/^www./.test(u)) {
            await checkPage("http://" + u);
        }
        else {
            await checkPage("http://www." + u);
        }
        
    }
}

fs.readFile('tovisit.csv', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    runCrawler(data.split("\n"));
});

