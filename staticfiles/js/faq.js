    const questionTitles = document.querySelectorAll('.question-title');

    questionTitles.forEach(title => {
      title.addEventListener('click', function() {
        this.parentElement.classList.toggle('active');
      });
    });