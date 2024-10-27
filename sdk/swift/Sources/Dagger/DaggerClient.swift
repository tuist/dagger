import Foundation

public final class DaggerClient: Sendable {
    let config: DaggerConfig
    let urlSession: URLSession
    let apiURL: URL
    
    init(config: DaggerConfig, apiURL: URL, urlSession: URLSession) {
        self.config = config
        self.apiURL = apiURL
        self.urlSession = urlSession
    }
    
    func query(_ query: String) async throws -> Any {
        var urlComponents = URLComponents(url: self.apiURL, resolvingAgainstBaseURL: false)!
        urlComponents.queryItems = [URLQueryItem(name: "query", value: query)]
        var request = URLRequest(url: urlComponents.url!)
        request.httpMethod = "POST"
        request.httpBody = try JSONSerialization.data(withJSONObject: ["query": query])
        request.allHTTPHeaderFields = [:]
        request.allHTTPHeaderFields?["Content-Type"] = "application/json"
        let (data, _) = try await urlSession.data(for: request)
        return try JSONSerialization.jsonObject(with: data)
    }
    
    public func container() -> Container {
        return Container(parent: .client(self))
    }

    
}
