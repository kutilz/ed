// dashboard.js
const app = {
    data() {
        return {
            isActive: false,
            attendance: {
                present: 24,
                total: 28,
                percentage: 85.71
            },
            engagement: {
                current: 76,
                history: [65, 72, 78, 69, 75, 76]
            },
            handRaises: 12,
            sessionDuration: '45:22',
            alerts: [
                {
                    type: 'warning',
                    message: 'Low attention detected in back row',
                    time: '2 minutes ago',
                    icon: 'exclamation-triangle'
                },
                {
                    type: 'info',
                    message: 'Student #15 left the classroom',
                    time: '5 minutes ago',
                    icon: 'person-dash'
                },
                {
                    type: 'success',
                    message: 'Hand raised by Student #7',
                    time: '8 minutes ago',
                    icon: 'hand-index-thumb'
                }
            ],
            students: [
                {
                    id: '#001',
                    name: 'John Smith',
                    status: 'present',
                    entryTime: '09:05 AM',
                    engagement: 85
                },
                {
                    id: '#002',
                    name: 'Jane Doe',
                    status: 'present',
                    entryTime: '08:58 AM',
                    engagement: 65
                },
                {
                    id: '#003',
                    name: 'David Johnson',
                    status: 'absent',
                    entryTime: '--:--',
                    engagement: 0
                },
                {
                    id: '#004',
                    name: 'Maria Garcia',
                    status: 'late',
                    entryTime: '09:22 AM',
                    engagement: 90
                },
                {
                    id: '#005',
                    name: 'Robert Chen',
                    status: 'present',
                    entryTime: '09:01 AM',
                    engagement: 45
                }
            ],
            detections: [
                {top: '20%', left: '30%', width: '10%', height: '15%', label: 'Student #12'},
                {top: '25%', left: '50%', width: '10%', height: '15%', label: 'Student #7'},
                {top: '60%', left: '70%', width: '10%', height: '15%', label: 'Student #19'}
            ]
        }
    },
    methods: {
        toggleSidebar() {
            this.isActive = !this.isActive;
            document.getElementById('sidebar').classList.toggle('active');
            document.getElementById('content').classList.toggle('active');
        },
        startSession() {
            // Code to start session
            console.log("Starting new session...");
        },
        viewDetails(studentId) {
            // Code to show student details
            console.log("Viewing details for:", studentId);
        },
        exportData() {
            // Code to export attendance data
            console.log("Exporting attendance data...");
        }
    },
    mounted() {
        // Initialize any components or fetch initial data
        console.log("Dashboard component mounted");
        
        // Set up WebSocket connection (mock)
        this.setupMockWebSocket();
    },
    methods: {
        setupMockWebSocket() {
            // Simulate real-time updates
            setInterval(() => {
                // Update engagement randomly
                const newEngagement = Math.floor(Math.random() * 20) + 65; // 65-85
                this.engagement.current = newEngagement;
                this.engagement.history.shift();
                this.engagement.history.push(newEngagement);
                
                // Update chart if it exists
                if (window.engagementChart) {
                    window.engagementChart.data.datasets[0].data = this.engagement.history;
                    window.engagementChart.update();
                }
                
                // Random chance to add a new alert
                if (Math.random() > 0.8) {
                    const alertTypes = ['warning', 'info', 'success', 'danger'];
                    const alertIcons = ['exclamation-triangle', 'person-dash', 'hand-index-thumb', 'activity'];
                    const randomType = alertTypes[Math.floor(Math.random() * alertTypes.length)];
                    const randomIcon = alertIcons[Math.floor(Math.random() * alertIcons.length)];
                    
                    this.alerts.unshift({
                        type: randomType,
                        message: `Random alert message ${Math.floor(Math.random() * 100)}`,
                        time: 'Just now',
                        icon: randomIcon
                    });
                    
                    // Keep only the most recent 3 alerts
                    if (this.alerts.length > 3) {
                        this.alerts.pop();
                    }
                }
            }, 5000); // Update every 5 seconds
        }
    }
};

// Initialize Vue app if Vue is available
if (typeof Vue !== 'undefined') {
    const vueApp = Vue.createApp(app);
    vueApp.mount('#app');
}