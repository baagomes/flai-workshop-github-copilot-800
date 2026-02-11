# OctoFit Tracker Frontend

A React-based fitness tracking application that connects to the Django REST API backend.

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── Activities.js    - Display user activities
│   │   ├── Leaderboard.js   - Competitive leaderboard with rankings
│   │   ├── Teams.js         - Team management and display
│   │   ├── Users.js         - User list and management
│   │   └── Workouts.js      - Personalized workout suggestions
│   ├── utils/
│   │   └── api.js           - API utility for constructing backend URLs
│   ├── App.js               - Main app component with routing
│   ├── App.css              - Application styles
│   └── index.js             - React entry point
├── public/                  - Static public files
├── .env                     - Environment variables
└── package.json             - Project dependencies
```

## Features

- **User Management**: View and manage user profiles
- **Team Functionality**: Create and manage fitness teams
- **Activity Logging**: Track fitness activities with calories and duration
- **Personalized Workouts**: Get workout suggestions based on user profile
- **Leaderboard**: Compete with others and track rankings
- **Responsive Navigation**: Bootstrap-based navigation menu with routing

## Setup Instructions

### 1. Install Dependencies

```bash
cd octofit-tracker/frontend
npm install
```

### 2. Environment Configuration

The frontend automatically detects whether it's running in a GitHub Codespace and constructs the appropriate API URL.

#### For GitHub Codespaces:

Set the `REACT_APP_CODESPACE_NAME` environment variable in the `.env` file:

```bash
REACT_APP_CODESPACE_NAME=your-codespace-name
```

The app will then use: `https://your-codespace-name-8000.app.github.dev/api/`

#### For Local Development:

The app defaults to `http://localhost:8000/api/` when `REACT_APP_CODESPACE_NAME` is not set.

### 3. Running the Development Server

```bash
npm start
```

The app will open in your browser at `http://localhost:3000`

### 4. Building for Production

```bash
npm build
```

This creates an optimized production build in the `build/` directory.

## Components

### Users Component
- Displays a list of all registered users
- Shows username, email, first name, and last name
- API Endpoint: `/api/users/`

### Teams Component
- Displays all teams with member counts
- Shows team descriptions and creation date
- API Endpoint: `/api/teams/`

### Activities Component
- Shows logged fitness activities
- Displays activity type, duration, calories burned
- API Endpoint: `/api/activities/`

### Workouts Component
- Shows personalized workout recommendations
- Displays workout type, difficulty, and duration
- API Endpoint: `/api/workouts/`

### Leaderboard Component
- Competitive ranking system
- Shows total calories burned and points
- Displays medal emojis for top 3 positions
- API Endpoint: `/api/leaderboard/`

## API Integration

All components use the `getAPIUrl()` utility function from `src/utils/api.js` to construct API endpoints.

### Features:
- **Dual Response Format Support**: Handles both paginated responses (`.results`) and plain arrays
- **Console Logging**: Each component logs:
  - The API endpoint being called
  - The raw response data
  - The processed data being rendered
- **Error Handling**: Displays user-friendly error messages if API calls fail
- **Loading States**: Shows loading indicators while fetching data

### Example API Call:
```javascript
const apiUrl = getAPIUrl('users');  // Returns: https://[codespace-name]-8000.app.github.dev/api/users/
console.log('Fetching from:', apiUrl);

const response = await fetch(apiUrl);
const data = await response.json();
const usersList = data.results ? data.results : data;
```

## Navigation

The app uses React Router v7 for navigation with the following routes:

- `/` - Home page with welcome message
- `/users` - User list
- `/teams` - Team management
- `/activities` - Activity log
- `/workouts` - Workout recommendations
- `/leaderboard` - Competitive leaderboard

## Styling

The frontend uses:
- **Bootstrap 5** for responsive UI components
- **Custom CSS** in `src/App.css` for additional styling
- **Responsive Design** that works on mobile, tablet, and desktop

## Troubleshooting

### API Connection Issues

**Check the console** for error messages:
```javascript
// Open browser DevTools (F12) and check Console tab
// You should see:
// "Fetching [component] from: https://..."
// "Data received: {...}"
// "Processed list: [...]"
```

**Verify Backend is Running:**
```bash
# Check if Django server is running on port 8000
curl http://localhost:8000/api/
```

**Check CODESPACE_NAME:**
```bash
# In your codespace terminal
echo $CODESPACE_NAME
```

### CORS Issues

If you see CORS errors in console, ensure the Django backend has CORS enabled:
- Backend should have `django-cors-headers` installed
- `CORS_ALLOWED_ORIGINS` should include your frontend URL

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `REACT_APP_CODESPACE_NAME` | GitHub Codespace name for production URLs | `my-codespace-abc123` |
| `REACT_APP_API_TIMEOUT` | Optional: API request timeout in ms | `5000` |

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

## Development

For development with hot reload:
```bash
npm start
```

The app will automatically reload when you save changes.

## Testing

Run tests with:
```bash
npm test
```

## Contributing

1. Create components in `src/components/`
2. Update routing in `src/App.js`
3. Use `getAPIUrl()` for API calls
4. Add console.log statements for debugging
5. Test with both localhost and codespace URLs

## Next Steps

- Implement user authentication (login/signup)
- Add form components for creating/updating data
- Implement real-time updates with WebSockets
- Add data filtering and sorting
- Create individual detail pages for resources
