const { exec } = require('child_process');

exec('./0-starwars_characters.js 3', (error, stdout, stderr) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`Stderr: ${stderr}`);
    return;
  }
  console.log(`Stdout:\n${stdout}`);
});
