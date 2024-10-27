import Foundation

/// Errors that can be thrown while conneting to the engine.
enum DaggerError: Error, Equatable, CustomStringConvertible {
    /// This error is thrown is the DAGGER_SESSION_PORT environment variable is absent.
    case missingPort(envVariable: String)
    /// This error is thrown if the DAGGER_SESSION_PORT environment variable is not a number.
    case invalidPortNumber(portString: String)
    /// This error is thrown if the DAGGER_SESSION_TOKEN environment variable is absent.
    case missingSessionToken(envVariable: String)

    var description: String {
        switch self {
        case .missingPort(let envVariable): return "The environment variable containing the Dagger session port, $\(envVariable), is absent."
        case .invalidPortNumber(let portString): return "The port value \(portString) is not a valid number."
        case .missingSessionToken(let envVariable): return "The environment variable containing the Dagger session token, $\(envVariable), is absent."
        }
    }
}

/// Dagger is the entry point to build
public final class Dagger: Sendable {
    /// Connects to the Dagger engine and returns a client instance to build a query from.
    /// - Parameter config: A configuration instance to configure the connection.
    /// - Returns: A client instance.
    public static func connect(config: DaggerConfig = DaggerConfig()) throws -> DaggerClient {
        return try self.connect(config: config, environment: ProcessInfo.processInfo.environment)
    }
    
    static func connect(config: DaggerConfig = DaggerConfig(),
                        environment: [String: String]) throws -> DaggerClient {
        guard let portString = environment["DAGGER_SESSION_PORT"] else {
            throw DaggerError.missingPort(envVariable: "DAGGER_SESSION_PORT")
        }
        guard let port = Int(portString) else {
            throw DaggerError.invalidPortNumber(portString: portString)
        }
        guard let sessionToken = environment["DAGGER_SESSION_TOKEN"] else {
            throw DaggerError.missingSessionToken(envVariable: "DAGGER_SESSION_TOKEN")
        }
        let apiURL = URL(string: "http://\(sessionToken):@127.0.0.1:\(port)/query")!
        return DaggerClient(config: config, apiURL: apiURL, urlSession: .shared)
    }
}
