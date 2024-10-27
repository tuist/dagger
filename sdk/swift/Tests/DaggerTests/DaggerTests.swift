import Foundation
import Testing
@testable import Dagger

struct DaggerTests {
    @Test func test_throws_when_dagger_session_port_is_absent() {
        // Given
        let environment: [String: String] = [:]
        
        // When
        #expect(throws: DaggerError.missingPort(envVariable: "DAGGER_SESSION_PORT"), performing: {
            try Dagger.connect(config: DaggerConfig(),
                                     environment: environment)
        })
    }
    
    @Test func test_throws_when_dagger_session_port_is_not_a_number() {
        // Given
        let environment: [String: String] = ["DAGGER_SESSION_PORT": "invalid"]
        
        // When/Then
        #expect(throws: DaggerError.invalidPortNumber(portString: "invalid"), performing: {
            try Dagger.connect(config: DaggerConfig(), environment: environment)
        })
    }
    
    @Test func test_throws_when_dagger_session_token_is_absent() {
        // Given
        let environment: [String: String] = ["DAGGER_SESSION_PORT": "1234"]
        
        // When/Then
        #expect(throws: DaggerError.missingSessionToken(envVariable: "DAGGER_SESSION_TOKEN"), performing: {
            try Dagger.connect(config: DaggerConfig(), environment: environment)
        })
    }
    
    @Test func test_returns_a_valid_client_instance_when_the_environment_is_valid() throws {
        // Given
        let environment: [String: String] = ["DAGGER_SESSION_PORT": "1234",
                                             "DAGGER_SESSION_TOKEN": "token"]
        let config = DaggerConfig()
        
        // When
        let client = try Dagger.connect(config: config, environment: environment)
        
        // Then
        #expect(client.config == config)
        #expect(client.apiURL == URL(string: "http://token:@127.0.0.1:1234/query")!)
    }
}
