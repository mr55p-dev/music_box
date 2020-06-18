function playAudio(fileName) {
  // document.getElementById('audioID').src(fileName);
  $('audio').attr('src', "/static/audio/"+fileName);
  $('audio')[0].play();
};
