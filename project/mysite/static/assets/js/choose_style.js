function previewImage(src) {
    const imageContainer = document.getElementById('imageContainer');
    const images = imageContainer.querySelectorAll('img');

    images.forEach(img => {
        img.addEventListener('click', function() {
            // Remove 'active' class from all images
            images.forEach(i => i.classList.remove('active'));
            
            // Add 'active' class to the clicked image
            this.classList.add('active');

            // Update preview image
            document.getElementById('TransImage').src = this.src;
        });
    });
}




