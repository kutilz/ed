import os
from pathlib import Path

def create_project_structure():
    # Direktori root proyek (eduvision/)
    base_path = Path('.')

    # Struktur direktori dan file
    structure = {
        'eduvision-frontend': {
            'assets': {
                'css': [],
                'js': [],
                'img': []
            },
            'components': [],
            'views': [],
            'files': ['index.html']
        },
        'eduvision-backend': {
            'models': [],
            'services': ['ai_processor.py', 'camera_service.py', 'analytics_service.py'],
            'static': [],
            'files': ['app.py', 'config.py', 'requirements.txt']
        },
        'root_files': ['README.md']
    }

    # Fungsi untuk membuat struktur direktori dan file
    def create_substructure(substructure, current_path):
        for key, value in substructure.items():
            if key == 'files':
                # Buat file di direktori saat ini
                for file_name in value:
                    file_path = current_path / file_name
                    if not file_path.exists():
                        file_path.touch()
                        print(f"Created file: {file_path}")
                        # Tambahkan konten default untuk file tertentu
                        if file_name == 'index.html':
                            with open(file_path, 'w') as f:
                                f.write('<!DOCTYPE html>\n<html>\n<head>\n    <title>EduVision</title>\n</head>\n<body>\n    <h1>Welcome to EduVision</h1>\n</body>\n</html>')
                        elif file_name == 'app.py':
                            with open(file_path, 'w') as f:
                                f.write('from flask import Flask, render_template\n'
                                        'from flask_socketio import SocketIO\n'
                                        'import os\n\n'
                                        'app = Flask(__name__)\n'
                                        'socketio = SocketIO(app)\n\n'
                                        '@app.route("/")\n'
                                        'def index():\n'
                                        '    return render_template("index.html")\n\n'
                                        'if __name__ == "__main__":\n'
                                        '    socketio.run(app, debug=True)\n')
                        elif file_name == 'config.py':
                            with open(file_path, 'w') as f:
                                f.write('# Configuration settings\n'
                                        'DEBUG = True\n'
                                        'SECRET_KEY = "your-secret-key"\n')
                        elif file_name == 'requirements.txt':
                            with open(file_path, 'w') as f:
                                f.write('flask\n'
                                        'flask-socketio\n'
                                        'python-socketio\n')
                    else:
                        print(f"Skipped file (already exists): {file_path}")
            elif isinstance(value, list):
                # Buat direktori
                dir_path = current_path / key
                dir_path.mkdir(exist_ok=True)
                print(f"Created directory: {dir_path}")
                # Buat file dalam direktori
                for file_name in value:
                    file_path = dir_path / file_name
                    if not file_path.exists():
                        file_path.touch()
                        print(f"Created file: {file_path}")
                    else:
                        print(f"Skipped file (already exists): {file_path}")
            elif isinstance(value, dict):
                # Buat direktori baru
                dir_path = current_path / key
                dir_path.mkdir(exist_ok=True)
                print(f"Created directory: {dir_path}")
                # Rekursi untuk isi direktori
                create_substructure(value, dir_path)

    # Buat file di root
    for file_name in structure.get('root_files', []):
        file_path = base_path / file_name
        if not file_path.exists():
            file_path.touch()
            print(f"Created file: {file_path}")
            if file_name == 'README.md':
                with open(file_path, 'w') as f:
                    f.write('# EduVision\n\nProyek untuk AI Vision dalam pengelolaan kelas.')
        else:
            print(f"Skipped file (already exists): {file_path}")

    # Buat struktur direktori dan file
    for dir_name, content in structure.items():
        if dir_name != 'root_files':
            dir_path = base_path / dir_name
            dir_path.mkdir(exist_ok=True)
            print(f"Created directory: {dir_path}")
            create_substructure(content, dir_path)

# Jalankan fungsi
if __name__ == '__main__':
    create_project_structure()