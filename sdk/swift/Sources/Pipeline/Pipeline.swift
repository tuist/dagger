import Foundation
import Dagger

@main
struct Pipeline {
    static func main() async throws {        
        let pythonVersion = try await Dagger.connect(config: DaggerConfig())
            .container()
            .from(address: "python")
            .withExec(args: ["python", "-V"])
            .stdout()
        print(pythonVersion)
    }
}
