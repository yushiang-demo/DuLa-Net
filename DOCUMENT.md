# APIs


## Quick start

- Start services `docker-compose up -d`
- Shutdown services `docker-compose down`
- Check services is alive `docker ps`
- Build Dockerfile if changed `docker-compose build`
- Get logs `docker-compose logs -f ${server, worker}`

## Workflow

Explore detailed information about the APIs in the Swagger UI documentation, accessible at http://localhost. The Swagger UI provides a comprehensive overview of the available APIs, including endpoints, methods, and detailed descriptions to assist you in understanding and interacting with the application.

In this repository, we've concentrated on building the AI service segment shown in the diagram below.

```mermaid
sequenceDiagram

    box User
    participant Frontend
    participant Data-Server
    end 
    
    box AI-Service
    participant AI-Server
    participant DuLa-Net
    participant Storage
    end

    Frontend->>+AI-Server: POST Task: { image, callbackURL(optional) }
    AI-Server ->>+ Storage: Create Folder: { id }
    Storage->>- AI-Server: Success
    AI-Server-->> Data-Server: Callback to update: { id, status:"initial" }
    AI-Server->> Frontend: Success: { id }
    AI-Server->>+DuLa-Net: Schedule Task: { id, image }
    DuLa-Net->>+Storage: Store Result: { id, image, result, metadata }
    Storage->>- DuLa-Net: Success
    DuLa-Net->>- AI-Server: Task Done: { result, status }
    AI-Server-->>- Data-Server: Callback to update: { id, result, status:"done" }

    Frontend->>+Data-Server: GET Task: { id }
    Data-Server->>-Frontend: { result, status }

    Frontend->>+AI-Server: Get Task: { id }
    AI-Server->>+Storage: Serve Static Files: { id }
    Storage->>-AI-Server: Success
    AI-Server->>-Frontend: Success: { id, links }
```


