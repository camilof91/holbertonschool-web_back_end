export function taskFirst() {
    // Use const as the value won't change
    const task = 'I prefer const when I can.';
    return task;
}

export function getLast() {
    return ' is okay';
}

export function taskNext() {
    // Use let as the value might be modified through concatenation
    let combination = 'But sometimes let';
    combination += getLast();

    return combination;
}
