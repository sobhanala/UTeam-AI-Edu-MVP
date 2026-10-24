import { FC, useState, useRef, useEffect } from "react";
import styles from "./chatbotPage.module.scss";
import sendIcon from "../../../public/icons/send-icon.svg";

interface Message {
  id: number;
  text: string;
  isUser: boolean;
  timestamp: Date;
}

const ChatbotPage: FC = () => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      text: "سلام! من چت بات هوشمند شما هستم. چطور می‌تونم کمکتون کنم؟",
      isUser: false,
      timestamp: new Date(),
    },
  ]);
  const [inputValue, setInputValue] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [newMessageId, setNewMessageId] = useState<number | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);

  const scrollToBottom = () => {
    // Since we're using flex-direction: column-reverse, we need to scroll to the top
    // to show the newest messages at the bottom
    const container = messagesEndRef.current?.parentElement;
    if (container) {
      container.scrollTop = 0;
    }
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Focus input on component mount and after sending messages
  useEffect(() => {
    if (inputRef.current && !isLoading) {
      inputRef.current.focus();
    }
  }, [isLoading]);

  // Focus input when component mounts
  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, []);

  const handleSendMessage = async () => {
    if (!inputValue.trim()) return;

    const userMessage: Message = {
      id: Date.now(),
      text: inputValue,
      isUser: true,
      timestamp: new Date(),
    };

    setNewMessageId(userMessage.id);
    setMessages((prev) => [...prev, userMessage]);
    setInputValue("");
    setIsLoading(true);

    // Simulate bot response
    setTimeout(() => {
      const botMessage: Message = {
        id: Date.now() + 1,
        text: "متشکرم از پیام شما. این یک پاسخ نمونه است. در نسخه کامل، اینجا پاسخ هوشمند از API دریافت می‌شود.",
        isUser: false,
        timestamp: new Date(),
      };
      setNewMessageId(botMessage.id);
      setMessages((prev) => [...prev, botMessage]);
      setIsLoading(false);
      
      // Clear the new message ID after animation completes
      setTimeout(() => {
        setNewMessageId(null);
      }, 300);
    }, 1000);
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };


  // return (

  // );

  return (
    <div className={styles.chatbotPage}>
      <div className={`${styles.chatbotPage} container`}>
        <div className={styles.chatHeader}>
          <h1>چت بات هوشمند</h1>
        </div>

        <div className={styles.chatContainer}>
          <div className={styles.messagesContainer}>
            {isLoading && (
              <div className={`${styles.message} ${styles.botMessage}`}>
                <div className={styles.messageContent}>
                  <div className={styles.typingIndicator}>
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </div>
              </div>
            )}

            {messages.slice().reverse().map((message, index) => (
              <div
                key={message.id}
                className={`${styles.message} ${
                  message.isUser ? styles.userMessage : styles.botMessage
                } ${newMessageId === message.id ? styles.newMessage : ''}`}
                style={{
                  animationDelay: newMessageId === message.id ? '0s' : `${index * 0.05}s`,
                }}
              >
                <div className={styles.messageContent}>
                  <div className={styles.messageText}>{message.text}</div>
                  <div className={styles.messageTime}>
                    {message.timestamp.toLocaleTimeString("fa-IR", {
                      hour: "2-digit",
                      minute: "2-digit",
                    })}
                  </div>
                </div>
              </div>
            ))}

            <div ref={messagesEndRef} />
          </div>

          <div className={styles.inputContainer}>
            <div className={styles.inputWrapper}>
              <textarea
                ref={inputRef}
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="پیام خود را بنویسید..."
                className={styles.messageInput}
                rows={1}
                disabled={isLoading}
              />
              <button
                onClick={handleSendMessage}
                disabled={!inputValue.trim() || isLoading}
                className={styles.sendButton}
              >
                <img src={sendIcon.src} alt="send" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatbotPage;
