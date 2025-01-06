const fs = Require('fs');
function decodeYValue(value, base) {
    return parseInt(value, base);
}
function lagrangeInterpolationAt0(points) {
    let k = points.length;
    let secret = 0;

    for (let i = 0; i < k; i++) {
        let [x_i, y_i] = points[i];

        let L_i_0 = 1;
        for (let j = 0; j < k; j++) {
            if (j !== i) {
                let [x_j, _] = points[j];
                L_i_0 *= (-x_j) / (x_i - x_j);
            }
        }
        secret += y_i * L_i_0;
    }

    return Math.round(secret);
}

function processTestCase(testCaseFile) {
    fs.readFile(testCaseFile, 'utf8', (err, data) => {
        if (err) {
            console.error(`Error reading file ${testCaseFile}:`, err);
            return;
        }

        const parsedData = JSON.parse(data);
        const points = [];

        console.log(`\nDecoding points for ${testCaseFile}:`);
        for (let key in parsedData) {
            if (key === 'keys') continue; 

            const root = parsedData[key];
            const base = parseInt(root.base);
            const value = root.value;
            const x = parseInt(key);  // The key is the x-coordinate
            const y = decodeYValue(value, base);
            points.push([x, y]);

            console.log(`Point for x = ${x}: (x = ${x}, y = ${y})`);
        }

        const secret = lagrangeInterpolationAt0(points);
        console.log(`Secret constant term for ${testCaseFile}: ${secret}\n`);
    });
}

const testCaseFiles = ['test_case_1.json', 'test_case_2.json'];

testCaseFiles.forEach((file) => {
    console.log(`Processing ${file}`);
    processTestCase(file);
});
