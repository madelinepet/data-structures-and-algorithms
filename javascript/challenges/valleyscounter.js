// count how many times a graph drops below sea level and forms a valley. One valley can have topography, but counts as a new valley if the line goes above sea level and back down

function count_valleys(topo) {
    // Input: str of Us and Ds to define topo
    // Output: int of nums of valleys
    var level = 0;
    var tracker = 0;
    topo = topo.split('');

    for(var i = 0; i < topo.length; i++) {
        if(topo[i] === 'u') {
            level += 1;
        }
        if(topo[i] === 'd') {
            level -= 1;
            if (level === -1) {
                tracker += 1;
            }
        }
    }
    return tracker;
}

count_valleys('dudduduudu');
