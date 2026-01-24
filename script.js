// Blog posts data - Add your blog posts here
const blogPosts = [
    {
        id: 1,
        title: "Getting Started with Web Development",
        excerpt: "A comprehensive guide to beginning your journey in web development. Learn the fundamentals and build your first website.",
        date: "Jan 20, 2025",
        category: "Tutorial",
        icon: "💻"
    },
    {
        id: 2,
        title: "The Art of Writing Clean Code",
        excerpt: "Discover best practices for writing maintainable, readable code that your future self will thank you for.",
        date: "Jan 18, 2025",
        category: "Development",
        icon: "✨"
    },
    {
        id: 3,
        title: "Building Modern Web Applications",
        excerpt: "Explore the latest trends and technologies in modern web application development and architecture.",
        date: "Jan 15, 2025",
        category: "Web Dev",
        icon: "🚀"
    },
    {
        id: 4,
        title: "Design Principles That Matter",
        excerpt: "Learn the fundamental principles of good design and how to apply them to your web projects.",
        date: "Jan 12, 2025",
        category: "Design",
        icon: "🎨"
    },
    {
        id: 5,
        title: "JavaScript Tips and Tricks",
        excerpt: "Master JavaScript with these essential tips, tricks, and patterns that every developer should know.",
        date: "Jan 10, 2025",
        category: "JavaScript",
        icon: "⚡"
    },
    {
        id: 6,
        title: "Responsive Design Essentials",
        excerpt: "Create websites that look great on any device with these responsive design techniques and strategies.",
        date: "Jan 8, 2025",
        category: "CSS",
        icon: "📱"
    }
];

// Function to create a post card
function createPostCard(post) {
    return `
        <article class="post-card" onclick="openPost(${post.id})">
            <div class="post-image">${post.icon}</div>
            <div class="post-content">
                <div class="post-meta">
                    <span class="post-date">${post.date}</span>
                    <span class="post-category">${post.category}</span>
                </div>
                <h3 class="post-title">${post.title}</h3>
                <p class="post-excerpt">${post.excerpt}</p>
                <a href="#" class="read-more" onclick="event.stopPropagation();">Read More</a>
            </div>
        </article>
    `;
}

// Function to render all posts
function renderPosts() {
    const postsGrid = document.getElementById('posts-grid');
    const postsHTML = blogPosts.map(post => createPostCard(post)).join('');
    postsGrid.innerHTML = postsHTML;
}

// Function to handle post click (you can customize this)
function openPost(postId) {
    const post = blogPosts.find(p => p.id === postId);
    if (post) {
        // For now, just alert. You can later navigate to a post detail page
        alert(`Opening: ${post.title}\n\nYou can create a separate page for this post or add a modal to display the full content.`);
        
        // Example: Navigate to a detail page
        // window.location.href = `post.html?id=${postId}`;
    }
}

// Initialize the blog when page loads
document.addEventListener('DOMContentLoaded', () => {
    renderPosts();
    
    // Add smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Add scroll animation trigger
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

// Observe all post cards
document.addEventListener('DOMContentLoaded', () => {
    const postCards = document.querySelectorAll('.post-card');
    postCards.forEach(card => observer.observe(card));
});