// Blog posts data - Add your blog posts here
const blogPosts = [
    {
        id: 1,
        title: "The Great Jungle Challenge: Complete AI Guide",
        excerpt: "The EPIC 5,600-line interactive adventure! Meet all 10 AI animals - Eagle (CNN), Elephant (LSTM), Lion (Transformer), Owl (BERT), Parrot (GPT), Giraffe (LLaMA), Twins (GAN), Chameleon (VAE), and Snail (Diffusion). Learn how every major AI works!",
        date: "Feb 4, 2025",
        category: "AI Deep Dive",
        icon: "🌴",
        url: "post-ai-jungle-complete.html"
    },
    {
        id: 2,
        title: "The Magical Jungle Translator: How Computers Learn Language",
        excerpt: "Join the animals of Transformer Forest as they discover the magical translation machine! Learn how AI understands and speaks through an enchanting story perfect for curious minds.",
        date: "Jan 25, 2025",
        category: "AI for Kids",
        icon: "🦁",
        url: "post-jungle-transformers.html"
    }
];

// Function to create a post card
function createPostCard(post) {
    const clickHandler = post.url ? `window.location.href='${post.url}'` : `openPost(${post.id})`;
    return `
        <article class="post-card" onclick="${clickHandler}">
            <div class="post-image">${post.icon}</div>
            <div class="post-content">
                <div class="post-meta">
                    <span class="post-date">${post.date}</span>
                    <span class="post-category">${post.category}</span>
                </div>
                <h3 class="post-title">${post.title}</h3>
                <p class="post-excerpt">${post.excerpt}</p>
                <a href="${post.url || '#'}" class="read-more" onclick="event.stopPropagation();">Read More</a>
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

// Function to handle post click
function openPost(postId) {
    const post = blogPosts.find(p => p.id === postId);
    if (post && post.url) {
        window.location.href = post.url;
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

// Observe all post cards after DOM loads
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const postCards = document.querySelectorAll('.post-card');
        postCards.forEach(card => observer.observe(card));
    }, 100);
});
