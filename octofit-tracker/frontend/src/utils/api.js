// API configuration utility
const getAPIUrl = (endpoint) => {
  // Get the codespace name from environment variable
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
  
  if (codespaceName) {
    return `https://${codespaceName}-8000.app.github.dev/api/${endpoint}/`;
  }
  
  // Fallback for local development
  return `http://localhost:8000/api/${endpoint}/`;
};

export default getAPIUrl;
