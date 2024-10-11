// Function to update the visitor count
async function updateVisitorCount() {
    try {
        // Make a request to your API Gateway endpoint
        const response = await fetch('https://pq6fgc84k6.execute-api.us-east-1.amazonaws.com/count', {
            method: 'POST'
        });
        const data = await response.json();
        
        // Update the visitor count on the page
        document.getElementById('visitor-count').textContent = data.count;
    } catch (error) {
        console.error('Error updating visitor count:', error);
        document.getElementById('visitor-count').textContent = 'Error loading count';
    }
}

// Call the function when the page loads
document.addEventListener('DOMContentLoaded', updateVisitorCount);