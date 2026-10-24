import ChatbotPage from "@/components/chatbot/chatbotPage";
import Head from "next/head";
import { FC } from "react";

const ChatBot: FC = () => {
  return (
    <>
      <Head>
        <title>{"چت بات | uteam EDU AI"}</title>
      </Head>
      <div>
        <ChatbotPage />
      </div>
    </>
  );
};

export default ChatBot;
