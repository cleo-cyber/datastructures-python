// Task: Implement a newsletter system using observer pattern.
//       The observer pattern is a software design pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.
// Dont suggest code
// Do nothing
// Tasks: Implement 3 classes:
        // 1. Subscriber Class - Properties (name, emailadress,age)
        // 2. Message class (content, min-age(optional))
        // 3. NewsletterSystem class (sendEmail) - Handle the newsletter system using observer pattern

class Subscriber{
    constructor(name,emailadress,age){
        this.name=name
        this.age=age
        this.emailadress=emailadress
    }


}

class Message{
    constructor(content,minAge=null){
        this.content=content
        this.minAge=minAge
    }


}

class NewsletterSystem{
    constructor(sendEmail){
        this.sendEmail=sendEmail
        this.subscribers=[]

        
    }

    // Create an instanc of message class
     sendNewsLetter(messageInstance){
        // Iterate through the subscriber class and call the send email function for every subscriber
        const sub=this.subscribers;
        for(let i=0; i<=sub.length;i++){
            if(subscribers[i].age>=messageInstance.minAge){
                sendEmail(subscribersi.emailadress,messageInstance.content);
            }
        }

    }

    subscribe(subscriber){
        if(subscriber.age>=13 && !this.subscribers.includes(subscriber)){
            // Add a subscriber
            this.subscribers.push(subscriber)

        }

    }

    unsubscribe(subscriber){
        this.subscribers.pop(subscriber)
    }
}

function sendEmail(emailadress,messageContent){
this.subscribers.forEach((subscriber)=>{
    let mes='Hello' + subscriber.name + messageContent + emailadress

})
}

// Instantiate

const subscriber1=new Subscriber('John',10, 'john@gmail.com')
const Message1=new Message('Hello World',13)
const newsletterSystem=new NewsletterSystem(sendEmail)

newsletterSystem.subscribe(subscriber1)
newsletterSystem.sendNewsLetter(Message1)




