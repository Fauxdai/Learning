// Dictionary to store notes
const notes = {
    'People': {},
    'Places': {},
    'Things that Happen': {},
    'Items': {},
    'History': {},
    'Knowledge': {},
    'Jokes': {}
};

document.addEventListener("DOMContentLoaded", function () {
    const logList = document.getElementById("logList");
    const addNoteButton = document.getElementById("addNote");
    const saveToTxtButton = document.getElementById("saveToTxt");

    addNoteButton.addEventListener("click", function () {
        const category = document.getElementById("category").value;
        const title = document.getElementById("title").value;
        const description = document.getElementById("description").value;

        if (title in notes[category]) {
            notes[category][title] += '\n' + description;
        } else {
            notes[category][title] = description;
        }

        document.getElementById("title").value = "";
        document.getElementById("description").value = "";

        updateLogList();
    });

    saveToTxtButton.addEventListener("click", function () {
        saveToTxtFile();
    });

    updateLogList();
});

function updateLogList() {
    const logList = document.getElementById("logList");
    logList.innerHTML = "";

    for (const category in notes) {
        for (const title in notes[category]) {
            const logEntry = document.createElement("div");
            logEntry.innerHTML = `<strong>Category:</strong> ${category}<br><strong>Title:</strong> ${title}<br><strong>Description:</strong> ${notes[category][title]}<hr>`;
            logList.appendChild(logEntry);
        }
    }
}

function saveToTxtFile() {
    const textToSave = Object.keys(notes)
        .map(category => {
            return Object.keys(notes[category])
                .map(title => `Category: ${category}\nTitle: ${title}\nDescription: ${notes[category][title]}\n`)
                .join('------------------\n');
        })
        .join('\n');

    const blob = new Blob([textToSave], { type: 'text/plain' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'notes.txt';
    a.style.display = 'none';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

