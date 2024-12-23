function showPage(page) {
    fetch(`/api/${page}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('content').innerHTML = renderPage(page, data);
        });
}

function renderPage(page, data) {
    if (page === 'events') {
        return data.map(event => `
            <div>
                <h2>${event.name}</h2>
                <p>${event.description}</p>
                <p>${event.location}</p>
                <p>${event.date}</p>
            </div>
        `).join('');
    }
    // Similar rendering for attendees and tasks
}
