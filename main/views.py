from django.shortcuts import render
import pandas as pd


def main_page(request):
    # Load the CSV file
    csv_file_path = 'main/templates/main/Song dataset.csv'
    song_data = pd.read_csv(csv_file_path)

    # Filter by mood if a mood is selected
    selected_mood = request.GET.get('mood', 'All')
    if selected_mood != 'All':
        filtered_songs = song_data[song_data['Mood'] == selected_mood]
    else:
        filtered_songs = song_data

    # Pass the filtered songs and selected mood to the template
    context = {
        'songs': filtered_songs.to_dict(orient='records'),  # Convert to list of dictionaries
        'mood': selected_mood,
        'moods': ['All', 'Sad', 'Happy', 'Motivation', 'Romantic', 'Friendship']  # Dropdown options
    }
    return render(request, 'main/main_page.html', context)
