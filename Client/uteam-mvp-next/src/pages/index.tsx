import Link from "next/link";

const Home = () => {
  return (
    <div className="home-page">
      <div className="container">
        <div className="home-content">
          <h1>خوش آمدید</h1>
          <Link href="/chatbot">
            <button className="chatbot-button">💬 چت بات هوشمند</button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Home;
