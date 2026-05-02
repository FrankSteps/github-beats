function sendVideoInfo() {
    const title = document.querySelector("h1.title yt-formatted-string")?.innerText || document.title;
    const url = window.location.href;
  
    fetch("http://localhost:8080/video", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, url })
    }).catch(err => console.log("Couldn't send to Python server", err));
  }
  
  // Envia a cada 5 segundos
  setInterval(sendVideoInfo, 8080);
  
