async function uploadAndPredict() {
    const inputElement = document.getElementById('imageInput');
    if (inputElement.files.length === 0) {
        alert('Please select an image file first.');
        return;
    }

    const file = inputElement.files[0];
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://localhost:8000/predict/', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error(`Server responded with a status of ${response.status}`);
        }

        const result = await response.json();
        const resultDiv = document.getElementById('predictionResult');
        resultDiv.innerHTML = `Prediction: ${result.class} with confidence: ${(result.confidence * 100).toFixed(2)}%`;
        resultDiv.style.display = 'block'; // Make the result visible

        // Wait 10 seconds before starting the fade out
        setTimeout(() => {
            resultDiv.style.opacity = '0';
        }, 3000);

        // After the transition ends, hide the element
        setTimeout(() => {
            resultDiv.style.display = 'none';
            resultDiv.style.opacity = '1'; // Reset opacity for next time
        }, 4000); // This should be 10s after the transition starts

    } catch (error) {
        console.error("Failed to send data to the backend:", error);
        alert("Failed to send data to the backend. Please check the console for more details.");
    }
}
