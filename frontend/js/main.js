document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate-btn');
    const sceneDescription = document.getElementById('scene-description');

    const resultsContainer = document.getElementById('results-container');
    const loader = document.getElementById('loader');
    const vignette = document.getElementById('vignette');
    const errorMessage = document.getElementById('error-message');

    const sceneImage = document.getElementById('scene-image');
    const sceneAudio = document.getElementById('scene-audio');
    const narrativeText = document.getElementById('narrative-text');

    generateBtn.addEventListener('click', async () => {
        const description = sceneDescription.value.trim();
        if (!description) {
            showError("please describe a scene first");
            return;
        }

        hideError();
        vignette.classList.add('hidden');
        resultsContainer.classList.remove('hidden');
        loader.classList.remove('hidden');

        try {
            const response = await fetch('/api/v1/generate-scene', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: description })

            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || "an unknown error occured")
            }

            const data = await response.json();

            sceneImage.src = data.image_url;
            sceneAudio.src = data.audio_url;
            narrativeText.textContent = `"${data.narrative}"`;

            loader.classList.add('hidden');
            vignette.classList.remove('hidden');
        } catch (error) {
            console.error('Error genrating scene :', error);
            showError(error.message);
            loader.classList.add('hidden');
        }
    });

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.remove('hidden');
    }
    function hideError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.remove('hidden');
    }
});