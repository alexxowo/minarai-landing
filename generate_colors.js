
function hexToRgb(hex) {
    const bigint = parseInt(hex.replace('#', ''), 16);
    return [(bigint >> 16) & 255, (bigint >> 8) & 255, bigint & 255];
}

function rgbToHex(r, g, b) {
    return "#" + ((1 << 24) + (Math.round(r) << 16) + (Math.round(g) << 8) + Math.round(b)).toString(16).slice(1);
}

function mixColor(c1, c2, weight) {
    const w1 = 1 - weight;
    const w2 = weight;
    return [
        c1[0] * w1 + c2[0] * w2,
        c1[1] * w1 + c2[1] * w2,
        c1[2] * w1 + c2[2] * w2
    ];
}

function generatePalette(baseHex, name) {
    const baseRgb = hexToRgb(baseHex);
    const white = [255, 255, 255];
    const black = [0, 0, 0];

    const shades = {
        50: [white, 0.95],
        100: [white, 0.9],
        200: [white, 0.75],
        300: [white, 0.6],
        400: [white, 0.3],
        500: [null, 0], // Base
        600: [black, 0.1],
        700: [black, 0.25],
        800: [black, 0.45],
        900: [black, 0.6],
        950: [black, 0.75],
    };

    console.log(`/* ${name} Palette */`);
    const steps = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950];
    
    steps.forEach(step => {
        let finalHex;
        if (step === 500) {
            finalHex = baseHex;
        } else {
            const [target, weight] = shades[step];
            const finalRgb = mixColor(baseRgb, target, weight);
            finalHex = rgbToHex(finalRgb[0], finalRgb[1], finalRgb[2]);
        }
        
        const kebabName = name.toLowerCase().replace(/ /g, "-");
        console.log(`  --color-${kebabName}-${step}: ${finalHex};`);
    });
    console.log("");
}

const colors = [
    ["#E9AD2F", "Golden Rod"],
    ["#28272A", "Black Beauty"],
    ["#AB0C29", "Barbados Cherry"],
    ["#2A512F", "Formal Garden"],
];

colors.forEach(([hex, name]) => generatePalette(hex, name));
