# AI Vision Classroom Assistant

![AI Vision Classroom Assistant Banner](project_banner.png)

## Overview

EduVision adalah perangkat berbasis NVIDIA Jetson Nano yang memanfaatkan computer vision dan AI untuk membantu pengajar dalam mengelola dan menganalisis dinamika kelas secara real-time. Sistem ini mampu mendeteksi kehadiran, gerakan, ekspresi, dan tingkat keterlibatan siswa menggunakan kamera yang dipasang di depan kelas.

$

## Fitur

- **Person Detection & Tracking**: Mendeteksi dan melacak siswa secara otomatis
- **Automatic Attendance**: Mencatat kehadiran siswa secara otomatis tanpa perlu absensi manual
- **Gesture Recognition**: Mengenali gestur tangan siswa, seperti mengangkat tangan
- **Expression Analysis**: Menganalisis ekspresi wajah untuk menilai tingkat pemahaman dan keterlibatan
- **Engagement Monitoring**: Mengukur tingkat perhatian siswa selama pembelajaran berlangsung
- **Web Dashboard**: Interface berbasis web yang dapat diakses oleh pengajar dalam jaringan lokal

## Arsitektur Sistem

Sistem ini terdiri dari beberapa komponen:

1. **Hardware**: NVIDIA Jetson Nano J1010, kamera wide-angle (8MP/160°), power adapter
2. **Software Pipeline**: Pemrosesan serial yang dioptimasi untuk komputasi terbatas
3. **AI Models**: YOLOv5-nano untuk deteksi, MediaPipe untuk gestur, MobileNet untuk ekspresi
4. **Web Interface**: Dashboard berbasis browser untuk pengajar

$

## Tata Letak Kelas

Perangkat AI Vision dipasang di bagian atas depan kelas (tengah) dengan field of view 160° yang mencakup seluruh ruangan berukuran 5x5m. Setup ini memungkinkan visualisasi dan analisis yang optimal terhadap aktivitas kelas.

$

## Pipeline Pemrosesan

Pipeline pemrosesan didesain secara serial untuk mengoptimalkan penggunaan resource terbatas pada Jetson Nano:

1. **Video Input**: Continuous capture dari kamera
2. **Pre-processing**: Resizing, frame skipping, ROI selection
3. **Person Detection & Tracking**: Dijalankan pada setiap frame
4. **Feature Analysis**: Dijalankan secara bergiliran (gestur, ekspresi)
5. **Analytics**: Pemrosesan background dengan prioritas rendah

$

## Diagram Alur Sistem

Berikut adalah sequence diagram yang menunjukkan interaksi antara komponen-komponen sistem:



## Entity Relationship Diagram

Berikut adalah struktur database yang digunakan dalam sistem:



## Implementasi Teknologi

### Hardware
- NVIDIA Jetson Nano J1010 (Seeed Studio)
- Kamera wide-angle 160° 8MP
- Power adapter

### Software Stack
- **OS**: Ubuntu (Jetson-compatible)
- **Framework AI**: TensorRT, OpenCV, MediaPipe
- **Backend**: Flask/FastAPI
- **Database**: SQLite/PostgreSQL
- **Frontend**: Vue.js + Chart.js
- **Komunikasi Real-time**: Socket.IO

## Optimasi Jetson Nano

Untuk memastikan performa optimal pada Jetson Nano yang memiliki keterbatasan daya komputasi:

1. **Model Optimization**:
   - TensorRT conversion untuk semua model
   - INT8/FP16 quantization
   - Model pruning untuk mengurangi ukuran
   
2. **Pipeline Efficiency**:
   - Frame skipping untuk mengurangi beban
   - Selective processing (ROI)
   - Task scheduling berdasarkan prioritas
   
3. **Memory Management**:
   - Zero-copy inference
   - Model sharing untuk mengoptimalkan penggunaan memory

## Instalasi dan Setup

### Prerequisites
- NVIDIA Jetson Nano j1010
- Python 3.13
- 8MP Camera
- WiFi/Ethernet

### Langkah Instalasi

1. Clone repository:
```bash
git clone https://github.com/kutilz/eduvision
cd eduvision
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Setup database:
```bash
python setup_db.py
```

4. Konfigurasi device:
```bash
nano config.yaml  # Edit sesuai kebutuhan
```

5. Jalankan server:
```bash
python app.py
```

6. Akses dashboard:
```
http://[IP_JETSON_NANO]:5000
```

## Roadmap Development

### Fase 1: Proof of Concept
- [x] Setup hardware dasar
- [ ] Implementasi person detection
- [x] Dashboard sederhana

### Fase 2: Core Features
- [ ] Gesture dan expression recognition
- [ ] Tracking kehadiran
- [ ] Integrasi dengan web interface

### Fase 3: Advanced Analytics
- [ ] Analisis engagement
- [ ] Fitur reporting
- [ ] Optimasi untuk performa real-time

## Lisensi

[MIT License](LICENSE).
